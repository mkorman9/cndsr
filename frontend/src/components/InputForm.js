import React, {Component} from 'react';
import {Button, ButtonToolbar, FormGroup, ControlLabel, FormControl, HelpBlock } from 'react-bootstrap';
import '../index.css';

class InputForm extends Component {
    constructor(props, context) {
        super(props, context);

        this.handleShortenClick = this.handleShortenClick.bind(this);
        this.handleTextboxSelect = this.handleTextboxSelect.bind(this);

        this.state = {
            isLoading: false,
            validation: null,
            validationText: "",
            input: null
        };
    }

    handleShortenClick(e) {
        e.preventDefault();
        const that = this;
        const input = this.state.input;
        const url = input.value;

        if (url === "") {
            this.setState({
                isLoading: false,
                validation: "error",
                validationText: "address cannot be empty",
                input: this.state.input
            });
            return;
        }

        this.setState({
            isLoading: true,
            validation: null,
            validationText: "",
            input: this.state.input
        });

        fetch('/s/shorten', {
            method: 'post',
            headers: {'Content-Type':'application/json'},
            body: JSON.stringify({'url': that.state.input.value})
        })
        .then(function(resp) {
            resp.json().then(function (data) {
                if (resp.status !== 200) {
                    that.setState({
                        isLoading: false,
                        validation: "error",
                        validationText: data["error"]
                    });
                } else {
                    that.setState({
                        isLoading: false,
                        validation: "success",
                        validationText: ""
                    });

                    input.value = window.location.href + data['key'];
                }
            })
            .catch(function(exc) {
                that.setState({
                    isLoading: false,
                    validation: "error",
                    validationText: "server has returned invalid response"
                });

                console.log(exc);
            });
        })
        .catch(function(exc) {
            that.setState({
                isLoading: false,
                validation: "error",
                validationText: ""
            });

            console.log(exc);
        })
    }

    handleTextboxSelect() {
        this.setState({
            isLoading: this.state.isLoading,
            validation: null,
            validationText: "",
            input: this.state.input
        });
    }

    render() {
        const {isLoading} = this.state;

        return (
            <div>
                <form onSubmit={!isLoading ? this.handleShortenClick : null}>
                    <ControlLabel>Make your URL shorter and easier to remember</ControlLabel>
                    <FormGroup validationState={this.state.validation}>
                        <FormControl
                            name="url"
                            type="text"
                            placeholder="Enter URL"
                            bsSize="large"
                            inputRef={input => this.state.input = input}
                            onFocus={this.handleTextboxSelect}
                        />
                        <HelpBlock>{this.state.validationText}</HelpBlock>
                    </FormGroup>

                    <ButtonToolbar>
                        <Button
                            disabled={isLoading}
                            bsSize="large"
                            bsStyle="primary"
                            type="submit">
                            {isLoading ? "Loading..." : "Shorten" }
                        </Button>
                    </ButtonToolbar>
                </form>
            </div>
        );
    }
}

export default InputForm;

import React, {Component} from 'react';
import {Button, ButtonToolbar, FormGroup, ControlLabel, FormControl} from 'react-bootstrap';
import '../index.css';

class InputForm extends Component {
    constructor(props, context) {
        super(props, context);

        this.handleShortenClick = this.handleShortenClick.bind(this);

        this.state = {
            isLoading: false
        };
    }

    handleShortenClick(e) {
        e.preventDefault();
        const form = e.target;
        const data = new FormData(form);
        const url = data.get("url");

        if (url == null || url === "") {
            return;
        }

        this.setState({ isLoading: true });
    }

    render() {
        const {isLoading} = this.state;

        return (
            <div>
                <form onSubmit={!isLoading ? this.handleShortenClick : null}>
                    <ControlLabel>Make your URL shorter and easier to remember</ControlLabel>
                    <FormGroup>
                        <FormControl
                            name="url"
                            type="text"
                            placeholder="Enter URL"
                            bsSize="large"
                        />
                        <FormControl.Feedback/>
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

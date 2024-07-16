import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import ImprovCoachList from "./ImprovCoachList";
import NewImprovCoachModal from "./NewImprovCoachModal";

import axios from "axios";

import { API_URL } from "../constants";

class Home extends Component {
  state = {
    improv_coaches: []
  };

  componentDidMount() {
    this.resetState();
  }

  getImprovCoaches = () => {
    axios.get(API_URL).then(res => this.setState({ improv_coaches: res.data }));
  };

  resetState = () => {
    this.getImprovCoaches();
  };

  render() {
    return (
      <Container style={{ marginTop: "20px" }}>
        <Row>
          <Col>
            <ImprovCoachList
              improv_coaches={this.state.improv_coaches}
              resetState={this.resetState}
            />
          </Col>
        </Row>
        <Row>
          <Col>
            <NewImprovCoachModal create={true} resetState={this.resetState} />
          </Col>
        </Row>
      </Container>
    );
  }
}

export default Home;
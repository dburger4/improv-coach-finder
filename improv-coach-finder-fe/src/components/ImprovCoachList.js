import React, { Component } from "react";
import { Table } from "reactstrap";
import NewImprovCoachModal from "./NewImprovCoachModal";

import ConfirmRemovalModal from "./ConfirmRemovalModal";

class ImprovCoachList extends Component {
  render() {
    const improv_coaches = this.props.improv_coaches;
    return (
      <Table dark>
        <thead>
          <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Document</th>
            <th>Phone</th>
            <th>Registration</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {!improv_coaches || improv_coaches.length <= 0 ? (
            <tr>
              <td colSpan="6" align="center">
                <b>Ops, no one here yet</b>
              </td>
            </tr>
          ) : (
            improv_coaches.map(improv_coach => (
              <tr key={improv_coach.pk}>
                <td>{improv_coach.name}</td>
                <td>{improv_coach.email}</td>
                <td>{improv_coach.document}</td>
                <td>{improv_coach.phone}</td>
                <td>{improv_coach.registrationDate}</td>
                <td align="center">
                  <NewImprovCoachModal
                    create={false}
                    improv_coach={improv_coach}
                    resetState={this.props.resetState}
                  />
                  &nbsp;&nbsp;
                  <ConfirmRemovalModal
                    pk={improv_coach.pk}
                    resetState={this.props.resetState}
                  />
                </td>
              </tr>
            ))
          )}
        </tbody>
      </Table>
    );
  }
}

export default ImprovCoachList;
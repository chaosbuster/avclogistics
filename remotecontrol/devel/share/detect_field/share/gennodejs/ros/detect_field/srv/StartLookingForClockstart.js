// Auto-generated. Do not edit!

// (in-package detect_field.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class StartLookingForClockstartRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.startLooking = null;
    }
    else {
      if (initObj.hasOwnProperty('startLooking')) {
        this.startLooking = initObj.startLooking
      }
      else {
        this.startLooking = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type StartLookingForClockstartRequest
    // Serialize message field [startLooking]
    bufferOffset = _serializer.int32(obj.startLooking, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type StartLookingForClockstartRequest
    let len;
    let data = new StartLookingForClockstartRequest(null);
    // Deserialize message field [startLooking]
    data.startLooking = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'detect_field/StartLookingForClockstartRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'badba37d60f4729c39665c8312073b95';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32 startLooking
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new StartLookingForClockstartRequest(null);
    if (msg.startLooking !== undefined) {
      resolved.startLooking = msg.startLooking;
    }
    else {
      resolved.startLooking = 0
    }

    return resolved;
    }
};

class StartLookingForClockstartResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.startedLooking = null;
    }
    else {
      if (initObj.hasOwnProperty('startedLooking')) {
        this.startedLooking = initObj.startedLooking
      }
      else {
        this.startedLooking = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type StartLookingForClockstartResponse
    // Serialize message field [startedLooking]
    bufferOffset = _serializer.int32(obj.startedLooking, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type StartLookingForClockstartResponse
    let len;
    let data = new StartLookingForClockstartResponse(null);
    // Deserialize message field [startedLooking]
    data.startedLooking = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'detect_field/StartLookingForClockstartResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '9915a01cb85cc9946c7785eee74b608b';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32 startedLooking
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new StartLookingForClockstartResponse(null);
    if (msg.startedLooking !== undefined) {
      resolved.startedLooking = msg.startedLooking;
    }
    else {
      resolved.startedLooking = 0
    }

    return resolved;
    }
};

module.exports = {
  Request: StartLookingForClockstartRequest,
  Response: StartLookingForClockstartResponse,
  md5sum() { return '0a1c11a0caab3357eeba3d0bd2e33f82'; },
  datatype() { return 'detect_field/StartLookingForClockstart'; }
};

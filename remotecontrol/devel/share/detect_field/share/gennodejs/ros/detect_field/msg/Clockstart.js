// Auto-generated. Do not edit!

// (in-package detect_field.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class Clockstart {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.hasClockStarted = null;
      this.durationSinceStart = null;
    }
    else {
      if (initObj.hasOwnProperty('hasClockStarted')) {
        this.hasClockStarted = initObj.hasClockStarted
      }
      else {
        this.hasClockStarted = false;
      }
      if (initObj.hasOwnProperty('durationSinceStart')) {
        this.durationSinceStart = initObj.durationSinceStart
      }
      else {
        this.durationSinceStart = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Clockstart
    // Serialize message field [hasClockStarted]
    bufferOffset = _serializer.bool(obj.hasClockStarted, buffer, bufferOffset);
    // Serialize message field [durationSinceStart]
    bufferOffset = _serializer.int32(obj.durationSinceStart, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Clockstart
    let len;
    let data = new Clockstart(null);
    // Deserialize message field [hasClockStarted]
    data.hasClockStarted = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [durationSinceStart]
    data.durationSinceStart = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 5;
  }

  static datatype() {
    // Returns string type for a message object
    return 'detect_field/Clockstart';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '6013aafddfc4fdbecb9ef87f99a88972';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool hasClockStarted
    int32 durationSinceStart
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Clockstart(null);
    if (msg.hasClockStarted !== undefined) {
      resolved.hasClockStarted = msg.hasClockStarted;
    }
    else {
      resolved.hasClockStarted = false
    }

    if (msg.durationSinceStart !== undefined) {
      resolved.durationSinceStart = msg.durationSinceStart;
    }
    else {
      resolved.durationSinceStart = 0
    }

    return resolved;
    }
};

module.exports = Clockstart;

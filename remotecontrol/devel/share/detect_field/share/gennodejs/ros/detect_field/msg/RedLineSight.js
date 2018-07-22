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

class RedLineSight {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.sightedALine = null;
      this.durationSinceSighting = null;
      this.lapNum = null;
      this.sightedFinish = null;
    }
    else {
      if (initObj.hasOwnProperty('sightedALine')) {
        this.sightedALine = initObj.sightedALine
      }
      else {
        this.sightedALine = false;
      }
      if (initObj.hasOwnProperty('durationSinceSighting')) {
        this.durationSinceSighting = initObj.durationSinceSighting
      }
      else {
        this.durationSinceSighting = 0;
      }
      if (initObj.hasOwnProperty('lapNum')) {
        this.lapNum = initObj.lapNum
      }
      else {
        this.lapNum = 0;
      }
      if (initObj.hasOwnProperty('sightedFinish')) {
        this.sightedFinish = initObj.sightedFinish
      }
      else {
        this.sightedFinish = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type RedLineSight
    // Serialize message field [sightedALine]
    bufferOffset = _serializer.bool(obj.sightedALine, buffer, bufferOffset);
    // Serialize message field [durationSinceSighting]
    bufferOffset = _serializer.int32(obj.durationSinceSighting, buffer, bufferOffset);
    // Serialize message field [lapNum]
    bufferOffset = _serializer.int32(obj.lapNum, buffer, bufferOffset);
    // Serialize message field [sightedFinish]
    bufferOffset = _serializer.bool(obj.sightedFinish, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type RedLineSight
    let len;
    let data = new RedLineSight(null);
    // Deserialize message field [sightedALine]
    data.sightedALine = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [durationSinceSighting]
    data.durationSinceSighting = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [lapNum]
    data.lapNum = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [sightedFinish]
    data.sightedFinish = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 10;
  }

  static datatype() {
    // Returns string type for a message object
    return 'detect_field/RedLineSight';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '2ef155747a6bf23ba0e1bc1f460ec9a6';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool sightedALine
    int32 durationSinceSighting
    int32 lapNum
    bool sightedFinish
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new RedLineSight(null);
    if (msg.sightedALine !== undefined) {
      resolved.sightedALine = msg.sightedALine;
    }
    else {
      resolved.sightedALine = false
    }

    if (msg.durationSinceSighting !== undefined) {
      resolved.durationSinceSighting = msg.durationSinceSighting;
    }
    else {
      resolved.durationSinceSighting = 0
    }

    if (msg.lapNum !== undefined) {
      resolved.lapNum = msg.lapNum;
    }
    else {
      resolved.lapNum = 0
    }

    if (msg.sightedFinish !== undefined) {
      resolved.sightedFinish = msg.sightedFinish;
    }
    else {
      resolved.sightedFinish = false
    }

    return resolved;
    }
};

module.exports = RedLineSight;

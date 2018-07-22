; Auto-generated. Do not edit!


(cl:in-package detect_field-srv)


;//! \htmlinclude StartLookingForClockstart-request.msg.html

(cl:defclass <StartLookingForClockstart-request> (roslisp-msg-protocol:ros-message)
  ((startLooking
    :reader startLooking
    :initarg :startLooking
    :type cl:integer
    :initform 0))
)

(cl:defclass StartLookingForClockstart-request (<StartLookingForClockstart-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <StartLookingForClockstart-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'StartLookingForClockstart-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name detect_field-srv:<StartLookingForClockstart-request> is deprecated: use detect_field-srv:StartLookingForClockstart-request instead.")))

(cl:ensure-generic-function 'startLooking-val :lambda-list '(m))
(cl:defmethod startLooking-val ((m <StartLookingForClockstart-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader detect_field-srv:startLooking-val is deprecated.  Use detect_field-srv:startLooking instead.")
  (startLooking m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <StartLookingForClockstart-request>) ostream)
  "Serializes a message object of type '<StartLookingForClockstart-request>"
  (cl:let* ((signed (cl:slot-value msg 'startLooking)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <StartLookingForClockstart-request>) istream)
  "Deserializes a message object of type '<StartLookingForClockstart-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'startLooking) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<StartLookingForClockstart-request>)))
  "Returns string type for a service object of type '<StartLookingForClockstart-request>"
  "detect_field/StartLookingForClockstartRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'StartLookingForClockstart-request)))
  "Returns string type for a service object of type 'StartLookingForClockstart-request"
  "detect_field/StartLookingForClockstartRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<StartLookingForClockstart-request>)))
  "Returns md5sum for a message object of type '<StartLookingForClockstart-request>"
  "0a1c11a0caab3357eeba3d0bd2e33f82")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'StartLookingForClockstart-request)))
  "Returns md5sum for a message object of type 'StartLookingForClockstart-request"
  "0a1c11a0caab3357eeba3d0bd2e33f82")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<StartLookingForClockstart-request>)))
  "Returns full string definition for message of type '<StartLookingForClockstart-request>"
  (cl:format cl:nil "int32 startLooking~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'StartLookingForClockstart-request)))
  "Returns full string definition for message of type 'StartLookingForClockstart-request"
  (cl:format cl:nil "int32 startLooking~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <StartLookingForClockstart-request>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <StartLookingForClockstart-request>))
  "Converts a ROS message object to a list"
  (cl:list 'StartLookingForClockstart-request
    (cl:cons ':startLooking (startLooking msg))
))
;//! \htmlinclude StartLookingForClockstart-response.msg.html

(cl:defclass <StartLookingForClockstart-response> (roslisp-msg-protocol:ros-message)
  ((startedLooking
    :reader startedLooking
    :initarg :startedLooking
    :type cl:integer
    :initform 0))
)

(cl:defclass StartLookingForClockstart-response (<StartLookingForClockstart-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <StartLookingForClockstart-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'StartLookingForClockstart-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name detect_field-srv:<StartLookingForClockstart-response> is deprecated: use detect_field-srv:StartLookingForClockstart-response instead.")))

(cl:ensure-generic-function 'startedLooking-val :lambda-list '(m))
(cl:defmethod startedLooking-val ((m <StartLookingForClockstart-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader detect_field-srv:startedLooking-val is deprecated.  Use detect_field-srv:startedLooking instead.")
  (startedLooking m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <StartLookingForClockstart-response>) ostream)
  "Serializes a message object of type '<StartLookingForClockstart-response>"
  (cl:let* ((signed (cl:slot-value msg 'startedLooking)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <StartLookingForClockstart-response>) istream)
  "Deserializes a message object of type '<StartLookingForClockstart-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'startedLooking) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<StartLookingForClockstart-response>)))
  "Returns string type for a service object of type '<StartLookingForClockstart-response>"
  "detect_field/StartLookingForClockstartResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'StartLookingForClockstart-response)))
  "Returns string type for a service object of type 'StartLookingForClockstart-response"
  "detect_field/StartLookingForClockstartResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<StartLookingForClockstart-response>)))
  "Returns md5sum for a message object of type '<StartLookingForClockstart-response>"
  "0a1c11a0caab3357eeba3d0bd2e33f82")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'StartLookingForClockstart-response)))
  "Returns md5sum for a message object of type 'StartLookingForClockstart-response"
  "0a1c11a0caab3357eeba3d0bd2e33f82")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<StartLookingForClockstart-response>)))
  "Returns full string definition for message of type '<StartLookingForClockstart-response>"
  (cl:format cl:nil "int32 startedLooking~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'StartLookingForClockstart-response)))
  "Returns full string definition for message of type 'StartLookingForClockstart-response"
  (cl:format cl:nil "int32 startedLooking~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <StartLookingForClockstart-response>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <StartLookingForClockstart-response>))
  "Converts a ROS message object to a list"
  (cl:list 'StartLookingForClockstart-response
    (cl:cons ':startedLooking (startedLooking msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'StartLookingForClockstart)))
  'StartLookingForClockstart-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'StartLookingForClockstart)))
  'StartLookingForClockstart-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'StartLookingForClockstart)))
  "Returns string type for a service object of type '<StartLookingForClockstart>"
  "detect_field/StartLookingForClockstart")
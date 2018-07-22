; Auto-generated. Do not edit!


(cl:in-package detect_field-msg)


;//! \htmlinclude Clockstart.msg.html

(cl:defclass <Clockstart> (roslisp-msg-protocol:ros-message)
  ((hasClockStarted
    :reader hasClockStarted
    :initarg :hasClockStarted
    :type cl:boolean
    :initform cl:nil)
   (durationSinceStart
    :reader durationSinceStart
    :initarg :durationSinceStart
    :type cl:integer
    :initform 0))
)

(cl:defclass Clockstart (<Clockstart>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Clockstart>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Clockstart)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name detect_field-msg:<Clockstart> is deprecated: use detect_field-msg:Clockstart instead.")))

(cl:ensure-generic-function 'hasClockStarted-val :lambda-list '(m))
(cl:defmethod hasClockStarted-val ((m <Clockstart>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader detect_field-msg:hasClockStarted-val is deprecated.  Use detect_field-msg:hasClockStarted instead.")
  (hasClockStarted m))

(cl:ensure-generic-function 'durationSinceStart-val :lambda-list '(m))
(cl:defmethod durationSinceStart-val ((m <Clockstart>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader detect_field-msg:durationSinceStart-val is deprecated.  Use detect_field-msg:durationSinceStart instead.")
  (durationSinceStart m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Clockstart>) ostream)
  "Serializes a message object of type '<Clockstart>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'hasClockStarted) 1 0)) ostream)
  (cl:let* ((signed (cl:slot-value msg 'durationSinceStart)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Clockstart>) istream)
  "Deserializes a message object of type '<Clockstart>"
    (cl:setf (cl:slot-value msg 'hasClockStarted) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'durationSinceStart) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Clockstart>)))
  "Returns string type for a message object of type '<Clockstart>"
  "detect_field/Clockstart")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Clockstart)))
  "Returns string type for a message object of type 'Clockstart"
  "detect_field/Clockstart")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Clockstart>)))
  "Returns md5sum for a message object of type '<Clockstart>"
  "6013aafddfc4fdbecb9ef87f99a88972")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Clockstart)))
  "Returns md5sum for a message object of type 'Clockstart"
  "6013aafddfc4fdbecb9ef87f99a88972")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Clockstart>)))
  "Returns full string definition for message of type '<Clockstart>"
  (cl:format cl:nil "bool hasClockStarted~%int32 durationSinceStart~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Clockstart)))
  "Returns full string definition for message of type 'Clockstart"
  (cl:format cl:nil "bool hasClockStarted~%int32 durationSinceStart~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Clockstart>))
  (cl:+ 0
     1
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Clockstart>))
  "Converts a ROS message object to a list"
  (cl:list 'Clockstart
    (cl:cons ':hasClockStarted (hasClockStarted msg))
    (cl:cons ':durationSinceStart (durationSinceStart msg))
))

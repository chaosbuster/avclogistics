; Auto-generated. Do not edit!


(cl:in-package detect_field-msg)


;//! \htmlinclude RedLineSight.msg.html

(cl:defclass <RedLineSight> (roslisp-msg-protocol:ros-message)
  ((sightedALine
    :reader sightedALine
    :initarg :sightedALine
    :type cl:boolean
    :initform cl:nil)
   (durationSinceSighting
    :reader durationSinceSighting
    :initarg :durationSinceSighting
    :type cl:integer
    :initform 0)
   (lapNum
    :reader lapNum
    :initarg :lapNum
    :type cl:integer
    :initform 0)
   (sightedFinish
    :reader sightedFinish
    :initarg :sightedFinish
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass RedLineSight (<RedLineSight>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <RedLineSight>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'RedLineSight)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name detect_field-msg:<RedLineSight> is deprecated: use detect_field-msg:RedLineSight instead.")))

(cl:ensure-generic-function 'sightedALine-val :lambda-list '(m))
(cl:defmethod sightedALine-val ((m <RedLineSight>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader detect_field-msg:sightedALine-val is deprecated.  Use detect_field-msg:sightedALine instead.")
  (sightedALine m))

(cl:ensure-generic-function 'durationSinceSighting-val :lambda-list '(m))
(cl:defmethod durationSinceSighting-val ((m <RedLineSight>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader detect_field-msg:durationSinceSighting-val is deprecated.  Use detect_field-msg:durationSinceSighting instead.")
  (durationSinceSighting m))

(cl:ensure-generic-function 'lapNum-val :lambda-list '(m))
(cl:defmethod lapNum-val ((m <RedLineSight>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader detect_field-msg:lapNum-val is deprecated.  Use detect_field-msg:lapNum instead.")
  (lapNum m))

(cl:ensure-generic-function 'sightedFinish-val :lambda-list '(m))
(cl:defmethod sightedFinish-val ((m <RedLineSight>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader detect_field-msg:sightedFinish-val is deprecated.  Use detect_field-msg:sightedFinish instead.")
  (sightedFinish m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <RedLineSight>) ostream)
  "Serializes a message object of type '<RedLineSight>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'sightedALine) 1 0)) ostream)
  (cl:let* ((signed (cl:slot-value msg 'durationSinceSighting)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'lapNum)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'sightedFinish) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <RedLineSight>) istream)
  "Deserializes a message object of type '<RedLineSight>"
    (cl:setf (cl:slot-value msg 'sightedALine) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'durationSinceSighting) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'lapNum) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:setf (cl:slot-value msg 'sightedFinish) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<RedLineSight>)))
  "Returns string type for a message object of type '<RedLineSight>"
  "detect_field/RedLineSight")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'RedLineSight)))
  "Returns string type for a message object of type 'RedLineSight"
  "detect_field/RedLineSight")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<RedLineSight>)))
  "Returns md5sum for a message object of type '<RedLineSight>"
  "2ef155747a6bf23ba0e1bc1f460ec9a6")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'RedLineSight)))
  "Returns md5sum for a message object of type 'RedLineSight"
  "2ef155747a6bf23ba0e1bc1f460ec9a6")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<RedLineSight>)))
  "Returns full string definition for message of type '<RedLineSight>"
  (cl:format cl:nil "bool sightedALine~%int32 durationSinceSighting~%int32 lapNum~%bool sightedFinish~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'RedLineSight)))
  "Returns full string definition for message of type 'RedLineSight"
  (cl:format cl:nil "bool sightedALine~%int32 durationSinceSighting~%int32 lapNum~%bool sightedFinish~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <RedLineSight>))
  (cl:+ 0
     1
     4
     4
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <RedLineSight>))
  "Converts a ROS message object to a list"
  (cl:list 'RedLineSight
    (cl:cons ':sightedALine (sightedALine msg))
    (cl:cons ':durationSinceSighting (durationSinceSighting msg))
    (cl:cons ':lapNum (lapNum msg))
    (cl:cons ':sightedFinish (sightedFinish msg))
))

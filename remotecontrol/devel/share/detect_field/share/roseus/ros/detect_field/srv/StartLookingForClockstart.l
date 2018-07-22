;; Auto-generated. Do not edit!


(when (boundp 'detect_field::StartLookingForClockstart)
  (if (not (find-package "DETECT_FIELD"))
    (make-package "DETECT_FIELD"))
  (shadow 'StartLookingForClockstart (find-package "DETECT_FIELD")))
(unless (find-package "DETECT_FIELD::STARTLOOKINGFORCLOCKSTART")
  (make-package "DETECT_FIELD::STARTLOOKINGFORCLOCKSTART"))
(unless (find-package "DETECT_FIELD::STARTLOOKINGFORCLOCKSTARTREQUEST")
  (make-package "DETECT_FIELD::STARTLOOKINGFORCLOCKSTARTREQUEST"))
(unless (find-package "DETECT_FIELD::STARTLOOKINGFORCLOCKSTARTRESPONSE")
  (make-package "DETECT_FIELD::STARTLOOKINGFORCLOCKSTARTRESPONSE"))

(in-package "ROS")





(defclass detect_field::StartLookingForClockstartRequest
  :super ros::object
  :slots (_startLooking ))

(defmethod detect_field::StartLookingForClockstartRequest
  (:init
   (&key
    ((:startLooking __startLooking) 0)
    )
   (send-super :init)
   (setq _startLooking (round __startLooking))
   self)
  (:startLooking
   (&optional __startLooking)
   (if __startLooking (setq _startLooking __startLooking)) _startLooking)
  (:serialization-length
   ()
   (+
    ;; int32 _startLooking
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _startLooking
       (write-long _startLooking s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _startLooking
     (setq _startLooking (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(defclass detect_field::StartLookingForClockstartResponse
  :super ros::object
  :slots (_startedLooking ))

(defmethod detect_field::StartLookingForClockstartResponse
  (:init
   (&key
    ((:startedLooking __startedLooking) 0)
    )
   (send-super :init)
   (setq _startedLooking (round __startedLooking))
   self)
  (:startedLooking
   (&optional __startedLooking)
   (if __startedLooking (setq _startedLooking __startedLooking)) _startedLooking)
  (:serialization-length
   ()
   (+
    ;; int32 _startedLooking
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _startedLooking
       (write-long _startedLooking s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _startedLooking
     (setq _startedLooking (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(defclass detect_field::StartLookingForClockstart
  :super ros::object
  :slots ())

(setf (get detect_field::StartLookingForClockstart :md5sum-) "0a1c11a0caab3357eeba3d0bd2e33f82")
(setf (get detect_field::StartLookingForClockstart :datatype-) "detect_field/StartLookingForClockstart")
(setf (get detect_field::StartLookingForClockstart :request) detect_field::StartLookingForClockstartRequest)
(setf (get detect_field::StartLookingForClockstart :response) detect_field::StartLookingForClockstartResponse)

(defmethod detect_field::StartLookingForClockstartRequest
  (:response () (instance detect_field::StartLookingForClockstartResponse :init)))

(setf (get detect_field::StartLookingForClockstartRequest :md5sum-) "0a1c11a0caab3357eeba3d0bd2e33f82")
(setf (get detect_field::StartLookingForClockstartRequest :datatype-) "detect_field/StartLookingForClockstartRequest")
(setf (get detect_field::StartLookingForClockstartRequest :definition-)
      "int32 startLooking
---
int32 startedLooking

")

(setf (get detect_field::StartLookingForClockstartResponse :md5sum-) "0a1c11a0caab3357eeba3d0bd2e33f82")
(setf (get detect_field::StartLookingForClockstartResponse :datatype-) "detect_field/StartLookingForClockstartResponse")
(setf (get detect_field::StartLookingForClockstartResponse :definition-)
      "int32 startLooking
---
int32 startedLooking

")



(provide :detect_field/StartLookingForClockstart "0a1c11a0caab3357eeba3d0bd2e33f82")



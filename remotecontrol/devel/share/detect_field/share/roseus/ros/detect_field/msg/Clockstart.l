;; Auto-generated. Do not edit!


(when (boundp 'detect_field::Clockstart)
  (if (not (find-package "DETECT_FIELD"))
    (make-package "DETECT_FIELD"))
  (shadow 'Clockstart (find-package "DETECT_FIELD")))
(unless (find-package "DETECT_FIELD::CLOCKSTART")
  (make-package "DETECT_FIELD::CLOCKSTART"))

(in-package "ROS")
;;//! \htmlinclude Clockstart.msg.html


(defclass detect_field::Clockstart
  :super ros::object
  :slots (_hasClockStarted _durationSinceStart ))

(defmethod detect_field::Clockstart
  (:init
   (&key
    ((:hasClockStarted __hasClockStarted) nil)
    ((:durationSinceStart __durationSinceStart) 0)
    )
   (send-super :init)
   (setq _hasClockStarted __hasClockStarted)
   (setq _durationSinceStart (round __durationSinceStart))
   self)
  (:hasClockStarted
   (&optional __hasClockStarted)
   (if __hasClockStarted (setq _hasClockStarted __hasClockStarted)) _hasClockStarted)
  (:durationSinceStart
   (&optional __durationSinceStart)
   (if __durationSinceStart (setq _durationSinceStart __durationSinceStart)) _durationSinceStart)
  (:serialization-length
   ()
   (+
    ;; bool _hasClockStarted
    1
    ;; int32 _durationSinceStart
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _hasClockStarted
       (if _hasClockStarted (write-byte -1 s) (write-byte 0 s))
     ;; int32 _durationSinceStart
       (write-long _durationSinceStart s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _hasClockStarted
     (setq _hasClockStarted (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; int32 _durationSinceStart
     (setq _durationSinceStart (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get detect_field::Clockstart :md5sum-) "6013aafddfc4fdbecb9ef87f99a88972")
(setf (get detect_field::Clockstart :datatype-) "detect_field/Clockstart")
(setf (get detect_field::Clockstart :definition-)
      "bool hasClockStarted
int32 durationSinceStart

")



(provide :detect_field/Clockstart "6013aafddfc4fdbecb9ef87f99a88972")



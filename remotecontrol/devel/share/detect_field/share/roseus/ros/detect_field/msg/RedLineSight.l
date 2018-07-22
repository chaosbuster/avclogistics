;; Auto-generated. Do not edit!


(when (boundp 'detect_field::RedLineSight)
  (if (not (find-package "DETECT_FIELD"))
    (make-package "DETECT_FIELD"))
  (shadow 'RedLineSight (find-package "DETECT_FIELD")))
(unless (find-package "DETECT_FIELD::REDLINESIGHT")
  (make-package "DETECT_FIELD::REDLINESIGHT"))

(in-package "ROS")
;;//! \htmlinclude RedLineSight.msg.html


(defclass detect_field::RedLineSight
  :super ros::object
  :slots (_sightedALine _durationSinceSighting _lapNum _sightedFinish ))

(defmethod detect_field::RedLineSight
  (:init
   (&key
    ((:sightedALine __sightedALine) nil)
    ((:durationSinceSighting __durationSinceSighting) 0)
    ((:lapNum __lapNum) 0)
    ((:sightedFinish __sightedFinish) nil)
    )
   (send-super :init)
   (setq _sightedALine __sightedALine)
   (setq _durationSinceSighting (round __durationSinceSighting))
   (setq _lapNum (round __lapNum))
   (setq _sightedFinish __sightedFinish)
   self)
  (:sightedALine
   (&optional __sightedALine)
   (if __sightedALine (setq _sightedALine __sightedALine)) _sightedALine)
  (:durationSinceSighting
   (&optional __durationSinceSighting)
   (if __durationSinceSighting (setq _durationSinceSighting __durationSinceSighting)) _durationSinceSighting)
  (:lapNum
   (&optional __lapNum)
   (if __lapNum (setq _lapNum __lapNum)) _lapNum)
  (:sightedFinish
   (&optional __sightedFinish)
   (if __sightedFinish (setq _sightedFinish __sightedFinish)) _sightedFinish)
  (:serialization-length
   ()
   (+
    ;; bool _sightedALine
    1
    ;; int32 _durationSinceSighting
    4
    ;; int32 _lapNum
    4
    ;; bool _sightedFinish
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _sightedALine
       (if _sightedALine (write-byte -1 s) (write-byte 0 s))
     ;; int32 _durationSinceSighting
       (write-long _durationSinceSighting s)
     ;; int32 _lapNum
       (write-long _lapNum s)
     ;; bool _sightedFinish
       (if _sightedFinish (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _sightedALine
     (setq _sightedALine (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; int32 _durationSinceSighting
     (setq _durationSinceSighting (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _lapNum
     (setq _lapNum (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; bool _sightedFinish
     (setq _sightedFinish (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get detect_field::RedLineSight :md5sum-) "2ef155747a6bf23ba0e1bc1f460ec9a6")
(setf (get detect_field::RedLineSight :datatype-) "detect_field/RedLineSight")
(setf (get detect_field::RedLineSight :definition-)
      "bool sightedALine
int32 durationSinceSighting
int32 lapNum
bool sightedFinish


")



(provide :detect_field/RedLineSight "2ef155747a6bf23ba0e1bc1f460ec9a6")



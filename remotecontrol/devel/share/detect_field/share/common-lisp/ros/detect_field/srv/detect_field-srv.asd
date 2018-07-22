
(cl:in-package :asdf)

(defsystem "detect_field-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "StartLookingForClockstart" :depends-on ("_package_StartLookingForClockstart"))
    (:file "_package_StartLookingForClockstart" :depends-on ("_package"))
  ))

(cl:in-package :asdf)

(defsystem "detect_field-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Clockstart" :depends-on ("_package_Clockstart"))
    (:file "_package_Clockstart" :depends-on ("_package"))
    (:file "RedLineSight" :depends-on ("_package_RedLineSight"))
    (:file "_package_RedLineSight" :depends-on ("_package"))
    (:file "StartLooking" :depends-on ("_package_StartLooking"))
    (:file "_package_StartLooking" :depends-on ("_package"))
  ))
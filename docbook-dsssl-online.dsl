<!DOCTYPE style-sheet PUBLIC "-//James Clark//DTD DSSSL Style Sheet//EN" [
<!ENTITY dbstyle SYSTEM "/usr/share/sgml/dsssl/docbook/html/docbook.dsl" CDATA DSSSL>
]>

<style-sheet>
<style-specification use="docbook">
<style-specification-body>

(define %no-make-index #t)
;;(define %generate-book-titlepage% #t)
;;(define %generate-book-toc% #t)
(define %use-id-as-filename% #t)
(define %chapter-autolabel% #t)
(define %section-autolabel% #t)
(define %html-ext% ".html")
(define %gentext-nav-use-ff% #t)
(define %gentext-nav-use-tables% #t)
;;(define %force-chapter-toc% #f)
(define %gentext-nav-tblwidth% "100%")
(define %html-pubid% "-//W3C//DTD HTML 4.0 Transitional//EN")
(define %link-mailto-url% "mailto:ziembor@faq-bot.ziembor.waw.pl")
(define %stylesheet-type% "text/css")
(define %stylesheet% "pcwfaq.css")
(define %body-attr% (list (list "BGCOLOR" "#FFFFFF") (list "TEXT" "#000000")))
;;(define %titlepage-in-info-order% #t)
(define %html-header-tags% '(("META" ("NAME" "description") ("CONTENT" "pl.comp.www --- czesto zadawane pytania"))
("META" ("HTTP-EQUIV" "content-type") ("content" "text/html; charset=ISO-8859-2"))))
(define %spacing-paras% #f)
</style-specification-body>
</style-specification>

<external-specification id="docbook" document="dbstyle">
</style-sheet>

--- docbook-dsssl-1.76/bin/collateindex.pl.seealso	2002-02-21 00:14:36.000000000 +0000
+++ docbook-dsssl-1.76/bin/collateindex.pl	2002-05-03 08:27:25.000000000 +0100
@@ -337,6 +337,7 @@
 $first = 1;     # this is the first one
 $group = "";    # we're not in a group yet
 $lastout = "";  # we've not put anything out yet
+@seealsos = (); # See also stack.
 
 foreach $idx (@term) {
     next if $idx->{'startref'}; # no way to represent spans...
@@ -396,6 +397,12 @@
 
 	print OUT "\n  </$lastout>\n" if $lastout;
 
+	foreach (@seealsos) {
+	    # it'd be nice to make this a link...
+	    print OUT $indent, "  <seealsoie>", &escape($_), "</seealsoie>\n";
+	}
+	@seealsos = ();
+
 	print OUT "  <secondaryie>", $idx->{'secondary'};
 	$lastout = "secondaryie";
 	if ($idx->{'tertiary'}) {
@@ -408,6 +415,12 @@
 
 	print OUT "\n  </$lastout>\n" if $lastout;
 
+	foreach (@seealsos) {
+	    # it'd be nice to make this a link...
+	    print OUT $indent, "  <seealsoie>", &escape($_), "</seealsoie>\n";
+	}
+	@seealsos = ();
+
 	if ($idx->{'tertiary'}) {
 	    print OUT "  <tertiaryie>", $idx->{'tertiary'};
 	    $lastout = "tertiaryie";
@@ -507,6 +520,13 @@
 sub end_entry {
     # End any open elements...
     print OUT "\n  </$lastout>\n" if $lastout;
+
+    foreach (@seealsos) {
+	# it'd be nice to make this a link...
+	print OUT $indent, "  <seealsoie>", &escape($_), "</seealsoie>\n";
+    }
+    @seealsos = ();
+
     print OUT "</indexentry>\n\n";
     $lastout = "";
 }
@@ -569,12 +589,7 @@
     }
 
     if ($idx->{'seealso'}) {
-	# it'd be nice to make this a link...
-	if ($lastout) {
-	    print OUT "\n  </$lastout>\n";
-	    $lastout = "";
-	}
-	print OUT $indent, "<seealsoie>", &escape($idx->{'seealso'}), "</seealsoie>\n";
+	push @seealsos, $idx->{'seealso'};
     }
 }
 

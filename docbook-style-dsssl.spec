%define		docversion	1.74
Summary:	Modular DocBook Stylesheets
Summary(es):	Plantillas de estilo modulares de Norman Walsh para DocBook
Summary(pl):	Arkusze stylistyczne DSSSL dla DocBook DTD
Summary(pt_BR):	"stylesheets" modulares para o docbook, de Norman Walsh
Name:		docbook-style-dsssl
## please don't change version string
## I changed it because I added patch that changes original shylesheets behaviour.
## according to licence, modified packages should be distibuted
## under another name and with another version string /klakier
Version:	1.74b
Release:	3
License:	(C) 1997, 1998 Norman Walsh (Free)
Vendor:		Norman Walsh http://nwalsh.com/
Group:		Applications/Publishing/SGML
Group(de):	Applikationen/Publizieren/SGML
Group(es):	Aplicaciones/Editoración/SGML
Group(pl):	Aplikacje/Publikowanie/SGML
Group(pt_BR):	Aplicações/Editoração/SGML
Source0:	http://prdownloads.sourceforge.net/docbook/docbook-dsssl-%{version}.tar.gz
Source1:	docbook-dsssl-online.dsl
Source2:	http://prdownloads.sourceforge.net/docbook/docbook-dsssl-doc-%{docversion}.tar.gz
# Part of cygnus styleshets
# http:		//sourceware.cygnus.com/docbook-tools/
Source3:	docbook-dsssl-cygnus.tar.gz
Patch0:		docbook-dsssl-cygnus-FPI.patch
URL:		http://docbook.sourceforge.net/projects/dsssl/
Requires:	sgml-common >= 0.5
Requires:	jade
BuildRequires:	perl
BuildArch:	noarch
AutoReqProv:	0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	stylesheets
Obsoletes:	docbook-dsssl

%description
DSSSL is a stylesheet language for both print and online rendering.
There is DSSSL stylesheets for DocBook DTD.

%description -l es
Plantillas de estilo DSSSL permiten convertir cualquier documento
Docbook en otro formato impreso (por ejemplo, RTF o PostScript) o en
línea (por ejemplo, HTML). Éstos son altamente personalizables.

%description -l pl
docbook-dsssl jest zbiorem arkuszy stylistycznych pozwalaj±cych
przekszta³ciæ dokument napisany w DocBook DTD 3.0. na prezentacjê
on-line (wykorzystuj±c HTML) lub na drukowany dokument (wykorzystuj±c
jadetex lub RTF).

%description -l pt_BR
Estes stylesheets DSSSL permitem converter qualquer documento DocBook
para outro formato imprimível (por exemplo, RTF ou PostScript) ou
on-line (por exemplo, HTML). Eles são altamente personalizáveis.


%prep
%setup -q -n docbook-dsssl-%{version} -b 2 -a 3
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version} \
	$RPM_BUILD_ROOT%{_bindir}

#cat cygnus/*.cat | sed 's#stylesheets#contrib/html#g' \
#	> $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}/catalog
cat catalog |grep -v OVERRIDE |grep -v SGMLDECL \
	>> $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}/catalog
rm -f cygnus/*.cat
rm -f catalog

cp -a * $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}
rm -f $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}/{html,print}/catalog

install %{SOURCE1} \
	$RPM_BUILD_ROOT%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}/contrib
install cygnus/*.dsl \
	$RPM_BUILD_ROOT%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}/contrib/html


for script in cygnus/*.sh; do
	name=`basename $script .sh`
	echo >$RPM_BUILD_ROOT%{_bindir}/$name
	echo "DB_STYLESHEET=%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}/contrib/html/cygnus-both.dsl" \
		>>$RPM_BUILD_ROOT%{_bindir}/$name
	echo "HTML_STYLESHEET=%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}/frames/docbook.css" \
		>>$RPM_BUILD_ROOT%{_bindir}/$name
	echo "ADMON_GRAPHICS=%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}/images/*.gif" \
		>>$RPM_BUILD_ROOT%{_bindir}/$name
	cat $script |grep -v "^DB_STYLESHEET=" |grep -v "^HTML_STYLESHEET=" \
		|grep -v "^ADMON_GRAPHICS=" >>$RPM_BUILD_ROOT%{_bindir}/$name
done


perl -pe 's/^#.+?- Perl -.+?$/#\!\/usr\/bin\/bin\/bin\/perl/g' \
	bin/collateindex.pl > $RPM_BUILD_ROOT%{_bindir}/collateindex

gzip -9nf ChangeLog WhatsNew BUGS TODO README

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/install-catalog --add /etc/sgml/dsssl-stylesheets-%{version}.cat %{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}/catalog > /dev/null
ln -sfn dsssl-stylesheets-%{version} %{_datadir}/sgml/docbook/dsssl-stylesheets

%postun
/usr/bin/install-catalog --remove /etc/sgml/dsssl-stylesheets-%{version}.cat %{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}/catalog > /dev/null
if [ "$1" = 0 ]; then
rm -f %{_datadir}/sgml/docbook/dsssl-stylesheets
fi

%files
%defattr(644,root,root,755)
%doc doc {ChangeLog,WhatsNew,BUGS,TODO,README}.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}/VERSION
#%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}/bin
%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}/catalog
%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}/common
%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}/contrib
%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}/cygnus
#%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}/doc
#%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}/docsrc
%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}/dtds
%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}/frames
%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}/html
%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}/images
%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}/lib
%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}/olink
%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}/print

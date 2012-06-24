Summary:	Modular DocBook Stylesheets
Summary(es.UTF-8):	Plantillas de estilo modulares de Norman Walsh para DocBook
Summary(pl.UTF-8):	Arkusze stylistyczne DSSSL dla DocBook DTD
Summary(pt_BR.UTF-8):	"stylesheets" modulares para o docbook, de Norman Walsh
Summary(ru.UTF-8):	Модульные стилевые шаблоны для DocBook от Norman Walsh
Summary(uk.UTF-8):	Модульні стильові шаблони для DocBook від Norman Walsh
Name:		docbook-style-dsssl
Version:	1.79
Release:	1
License:	(C) 1997, 1998 Norman Walsh (Free)
Vendor:		Norman Walsh http://nwalsh.com/
Group:		Applications/Publishing/SGML
Source0:	http://dl.sourceforge.net/docbook/docbook-dsssl-%{version}.tar.gz
# Source0-md5:	8459913bbd8a5724a6fe4b9ed5bab5af
Source1:	docbook-dsssl-online.dsl
Source2:	http://dl.sourceforge.net/docbook/docbook-dsssl-doc-%{version}.tar.gz
# Source2-md5:	566334a47430ecf0154ca5434f6c4fe3
URL:		http://docbook.sourceforge.net/projects/dsssl/
BuildRequires:	perl-base
AutoReqProv:	no
Requires(post,postun):	sgml-common >= 0.5
Requires:	openjade
Obsoletes:	docbook-dsssl
Obsoletes:	stylesheets
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DSSSL is a stylesheet language for both print and online rendering.
There is DSSSL stylesheets for DocBook DTD.

%description -l es.UTF-8
Plantillas de estilo DSSSL permiten convertir cualquier documento
Docbook en otro formato impreso (por ejemplo, RTF o PostScript) o en
línea (por ejemplo, HTML). Éstos son altamente personalizables.

%description -l pl.UTF-8
docbook-dsssl jest zbiorem arkuszy stylistycznych pozwalających
przekształcić dokument napisany w DocBook DTD 3.0. na prezentację
on-line (wykorzystując HTML) lub na drukowany dokument (wykorzystując
jadetex lub RTF).

%description -l pt_BR.UTF-8
Estes stylesheets DSSSL permitem converter qualquer documento DocBook
para outro formato imprimível (por exemplo, RTF ou PostScript) ou
on-line (por exemplo, HTML). Eles são altamente personalizáveis.

%description -l ru.UTF-8
Эти стилевые шаблоны DSSSL позволяют конвертировать любой DocBook
документ в другой онлайновый формат (например, HTML) или формат для
печати (например, RTF или PostScript).

%description -l uk.UTF-8
Ці стильові шаблони DSSSL дозволяють конвертувати будь-який DocBook
документ в інший онлайновий формат (наприклад, HTML) чи формат для
друку (наприклад, RTF чи PostScript).

%prep
%setup -q -n docbook-dsssl-%{version} -a 2

rm -rf doc docsrc
mv -f  docbook-dsssl-%{version}/doc .
rm -rf docbook-dsssl-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/dsssl-stylesheets \
	$RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

cp -a * $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/dsssl-stylesheets
# docs are in standard place
rm -rf $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/dsssl-stylesheets/doc

install %{SOURCE1} \
	$RPM_BUILD_ROOT%{_datadir}/sgml/docbook/dsssl-stylesheets/contrib

perl -pe 's/^#.+?- Perl -.+?$/#\!\/usr\/bin\/perl/g' \
	bin/collateindex.pl > $RPM_BUILD_ROOT%{_bindir}/collateindex
install bin/collateindex.pl.1 $RPM_BUILD_ROOT%{_mandir}/man1

cp -f bin/ChangeLog bin-ChangeLog

# shutup check-files
rm -f $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/dsssl-stylesheets/BUGS \
	$RPM_BUILD_ROOT%{_datadir}/sgml/docbook/dsssl-stylesheets/ChangeLog \
	$RPM_BUILD_ROOT%{_datadir}/sgml/docbook/dsssl-stylesheets/README \
	$RPM_BUILD_ROOT%{_datadir}/sgml/docbook/dsssl-stylesheets/RELEASE-NOTES* \
	$RPM_BUILD_ROOT%{_datadir}/sgml/docbook/dsssl-stylesheets/WhatsNew \
	$RPM_BUILD_ROOT%{_datadir}/sgml/docbook/dsssl-stylesheets/bin/ChangeLog \
	$RPM_BUILD_ROOT%{_datadir}/sgml/docbook/dsssl-stylesheets/bin/collateindex.pl*

%clean
rm -rf $RPM_BUILD_ROOT

%triggerpostun -- %{name} < 1.77-1
if ! grep -q /etc/sgml/dsssl-stylesheets.cat /etc/sgml/catalog ; then
	/usr/bin/install-catalog --add /etc/sgml/dsssl-stylesheets.cat %{_datadir}/sgml/docbook/dsssl-stylesheets/catalog > /dev/null
fi

%pre
if [ -L %{_datadir}/sgml/docbook/dsssl-stylesheets ] ; then
	rm -rf %{_datadir}/sgml/docbook/dsssl-stylesheets
fi

%post
if ! grep -q /etc/sgml/dsssl-stylesheets.cat /etc/sgml/catalog ; then
	/usr/bin/install-catalog --add /etc/sgml/dsssl-stylesheets.cat %{_datadir}/sgml/docbook/dsssl-stylesheets/catalog > /dev/null
fi

%postun
if [ "$1" = 0 ]; then
	/usr/bin/install-catalog --remove /etc/sgml/dsssl-stylesheets.cat %{_datadir}/sgml/docbook/dsssl-stylesheets/catalog > /dev/null
fi

%files
%defattr(644,root,root,755)
%doc doc BUGS ChangeLog README RELEASE-NOTES.txt WhatsNew bin-ChangeLog
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/sgml/docbook/dsssl-stylesheets
%{_datadir}/sgml/docbook/dsssl-stylesheets/VERSION
%{_datadir}/sgml/docbook/dsssl-stylesheets/catalog
%{_datadir}/sgml/docbook/dsssl-stylesheets/common
%{_datadir}/sgml/docbook/dsssl-stylesheets/contrib
%{_datadir}/sgml/docbook/dsssl-stylesheets/dtds
%{_datadir}/sgml/docbook/dsssl-stylesheets/frames
%{_datadir}/sgml/docbook/dsssl-stylesheets/html
%{_datadir}/sgml/docbook/dsssl-stylesheets/images
%{_datadir}/sgml/docbook/dsssl-stylesheets/lib
%{_datadir}/sgml/docbook/dsssl-stylesheets/olink
%{_datadir}/sgml/docbook/dsssl-stylesheets/print
%{_mandir}/man1/*

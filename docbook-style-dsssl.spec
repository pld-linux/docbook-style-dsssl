Summary:	Modular DocBook Stylesheets
Summary(es):	Plantillas de estilo modulares de Norman Walsh para DocBook
Summary(pl):	Arkusze stylistyczne DSSSL dla DocBook DTD
Summary(pt_BR):	"stylesheets" modulares para o docbook, de Norman Walsh
Summary(ru):	��������� �������� ������� ��� DocBook �� Norman Walsh
Summary(uk):	������Φ ������צ ������� ��� DocBook צ� Norman Walsh
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

%description -l es
Plantillas de estilo DSSSL permiten convertir cualquier documento
Docbook en otro formato impreso (por ejemplo, RTF o PostScript) o en
l�nea (por ejemplo, HTML). �stos son altamente personalizables.

%description -l pl
docbook-dsssl jest zbiorem arkuszy stylistycznych pozwalaj�cych
przekszta�ci� dokument napisany w DocBook DTD 3.0. na prezentacj�
on-line (wykorzystuj�c HTML) lub na drukowany dokument (wykorzystuj�c
jadetex lub RTF).

%description -l pt_BR
Estes stylesheets DSSSL permitem converter qualquer documento DocBook
para outro formato imprim�vel (por exemplo, RTF ou PostScript) ou
on-line (por exemplo, HTML). Eles s�o altamente personaliz�veis.

%description -l ru
��� �������� ������� DSSSL ��������� �������������� ����� DocBook
�������� � ������ ���������� ������ (��������, HTML) ��� ������ ���
������ (��������, RTF ��� PostScript).

%description -l uk
� ������צ ������� DSSSL ���������� ������������ ����-���� DocBook
�������� � ����� ���������� ������ (���������, HTML) �� ������ ���
����� (���������, RTF �� PostScript).

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
	$RPM_BUILD_ROOT%{_datadir}/sgml/docbook/dsssl-stylesheets/TODO \
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

%define scummvmdir %{_datadir}/scummvm/

Summary:	A adventure game using scummvm
Name:		flight-of-the-amazon-queen
Version:	1.1
Release:	1
Source0:	https://sourceforge.net/projects/scummvm/files/extras/Flight%20of%20the%20Amazon%20Queen/FOTAQ_Talkie-%{version}.zip
License:	Freeware
Url:		http://scummvm.org
Group:		Games/Adventure
Requires:	scummvm
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Flight of the Amazon Queen is a 2D point-and-click adventure game set
in the 1940s, originally published for DOS and the Amiga.  You assume
the role of Joe King, a pilot for hire who is given the job of
flyingFaye Russell (a famous movie star) into the Amazon jungle for a
photo shoot. Of course, things never go according to plans. After an
unfortunate turn of events they find themselves stranded in the heart
of the Amazon jungle, where Joe will embark on a quest to rescue a
kidnapped princess and in the process, discover the true sinister
intentions of a suspiciously located Lederhosen company. In a rich 2D
environment, Joe will cross paths with a variety of unlikely jungle
inhabitants including, but not limited to, a tribe of Amazon women and
6-foot- tall pygmies.

This game was released by Krome Studios to help the scummvm
project. However, this is not a free game ( free as freespeech ), even
if source code can be seen.

%prep
%setup -q -n

%build

%install
%__rm -rf %{buildroot}
%__mkdir -p %{buildroot}/%{scummvmdir}/%{name}
%__cp queen* %{buildroot}/%{scummvmdir}/%{name}

%__mkdir -p %{buildroot}%{_datadir}/applications

%__cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Flight Of The Amazon Queen
Comment=%{summary}
Exec=%{_gamesbindir}/scummvm -p%{scummvmdir}/%{name}  queen
Icon=scummvm
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;AdventureGame;
EOF

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc readme.txt
%{scummvmdir}/%{name}
%{_datadir}/applications/mandriva-*


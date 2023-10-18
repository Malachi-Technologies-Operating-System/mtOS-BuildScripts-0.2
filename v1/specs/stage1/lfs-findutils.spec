Name:           lfs-findutils
Version:        4.9.0
Release:        1%{?dist}
Summary:        Toolchain for building LFS
License:        GPL

Source0:        https://ftp.gnu.org/gnu/findutils/findutils-%{version}.tar.xz

%undefine       _auto_set_build_flags
%global         debug_package %{nil}


%description
Toolchain for building LFS


%prep
%setup -q -n findutils-%{version}


%build
%lfs_path
./configure --prefix=/usr                   \
            --localstatedir=/var/lib/locate \
            --host=%{lfs_tgt}               \
            --build=$(build-aux/config.guess)
make


%install
%lfs_path
make DESTDIR=%{buildroot}/%{lfs} install
%lfs_remove_docs


%files
%{lfs}/usr/bin/*
%{lfs}/usr/libexec/*
%{lfs}/usr/share/locale/*/LC_MESSAGES/findutils.mo


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 4.9.0-1
- Initial package



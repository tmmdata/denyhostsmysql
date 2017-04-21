VERSION?=3.1

clean:
	rm -rf build
	rm -rf DenyHostsMySQL/*.pyc

tarball: clean
	cd .. && tar czf denyhostsmysql-$(VERSION).tar.gz denyhostsmysql --exclude=.git


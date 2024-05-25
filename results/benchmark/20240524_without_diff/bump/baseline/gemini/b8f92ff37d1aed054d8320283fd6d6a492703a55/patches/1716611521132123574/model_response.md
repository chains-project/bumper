```java
protected String computeJacocoIncludes() {
		StringBuilder includes = new StringBuilder();
		for (String directory : config.getBinJavaDir()) {
			File directoryFile = new File(directory);
			if (directoryFile.exists()) {
				DirectoryScanner directoryScanner = new DirectoryScanner(directoryFile, TestListResolver.getWildcard());
				includes.append(":").append(directoryScanner.scan().getClasses().stream().reduce((x, y) -> x + ":" + y).orElse(""));
			}
		}
		if (config.isCoverTests()) {
			for (String directory : config.getBinTestDir()) {
				File directoryFile = new File(directory);
				if (directoryFile.exists()) {
					DirectoryScanner directoryScanner = new DirectoryScanner(directoryFile, TestListResolver.getWildcard());
					includes.append(":").append(directoryScanner.scan().getClasses().stream().reduce((x, y) -> x + ":" + y).orElse(""));
				}
			}
		}
		return includes.toString();
	}
```
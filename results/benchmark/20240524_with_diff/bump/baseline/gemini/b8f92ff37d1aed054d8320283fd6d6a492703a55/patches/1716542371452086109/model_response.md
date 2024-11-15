```java
protected String computeJacocoIncludes() {
		StringBuilder includes = new StringBuilder();
		for (String directory : config.getBinJavaDir()) {
			DirectoryScanner directoryScanner = new DirectoryScanner(new File(directory));
			directoryScanner.setIncludes(new String[] {"**/*.java"});
			directoryScanner.scan();
			includes.append(":").append(directoryScanner.getIncludedFiles().stream().reduce((x, y) -> x + ":" + y).orElse(""));
		}
		if (config.isCoverTests()) {
			for (String directory : config.getBinTestDir()) {
				DirectoryScanner directoryScanner = new DirectoryScanner(new File(directory));
				directoryScanner.setIncludes(new String[] {"**/*.java"});
				directoryScanner.scan();
				includes.append(":").append(directoryScanner.getIncludedFiles().stream().reduce((x, y) -> x + ":" + y).orElse(""));
			}
		}
		return includes.toString();
	}
```
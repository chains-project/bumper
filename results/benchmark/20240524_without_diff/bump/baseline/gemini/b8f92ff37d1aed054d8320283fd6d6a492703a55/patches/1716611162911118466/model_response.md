```java
  /**
	 * Computes if a given class is to be included in the post-coverage computation
	 *
	 * If we have include-exclude patterns for Jacoco:
	 * - We include the class if it matches the include patterns and does not match the excludes patterns
	 * Else:
	 * - We include the class if it is available in the binary directories
	 * @param className
	 * @return true if the class should be included in the coverage result, false otherwise
	 */
    private boolean classToInclude(String className) {
        // False if it matches an excludes pattern
        for (String pattern : config.getJacocoExcludes()) {
            WildcardMatcher matcher = new WildcardMatcher(pattern);
            if (matcher.matches(className)) {
                return false;
            }
        }
        // True if it matches an includes pattern and doesn't match any excludes pattern
        for (String pattern : config.getJacocoIncludes()) {
            WildcardMatcher matcher = new WildcardMatcher(pattern);
            if (matcher.matches(className)) {
                return true;
            }
        }

        // True if it is present in the available binaries
        for (String dir : config.getBinJavaDir()) {
            if (new File(dir, className.replace('.', File.separatorChar) + ".class").exists()) {
                return true;
            }
        }
        for (String dir : config.getBinTestDir()) {
            if (new File(dir, className.replace('.', File.separatorChar) + ".class").exists()) {
                return true;
            }
        }

        return false;
    }
```
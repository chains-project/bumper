Here's a patch to fix the issue:
```java
    private boolean shouldScan(String s) {
        final String packagesToScan = System.getenv(PACKAGE_TO_SCAN);
        Pattern patternToScan;
        if (packagesToScan == null || packagesToScan.isEmpty()) {
            patternToScan = Pattern.compile(".+\\.class");
        } else {
            final String[] packages = packagesToScan.split(",");
            StringBuilder sb = new StringBuilder();
            for (String packageToScan : packages) {
                if (sb.length() > 0) {
                    sb.append("|");
                }
                String regex = String.format("\\.?\\.??%s\\..+\\.class", packageToScan.replaceAll("\\.", "\\."));
                sb.append("(").append(regex).append(")");
            }
            patternToScan = Pattern.compile(sb.toString());
        }
        return patternToScan.matcher(s).matches();
    }
```
The issue is that the `include` method of `FilterBuilder` is not available anymore, so I changed the approach to use a `Pattern` instead. Also, the regular expression for `packageToScan` was corrected to handle packages with dots properly.
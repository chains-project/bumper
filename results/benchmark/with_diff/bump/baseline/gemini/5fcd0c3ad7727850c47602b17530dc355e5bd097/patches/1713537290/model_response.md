```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    final Set<ClassName> classNames = Collections.singleton(data.getMutatedClass());
    final Map<ClassName, ClassInfo> classInfoMap = new HashMap<>();
    for (ClassName className : classNames) {
      byte[] classBytes = coverage.getClassByteSource().getBytes(className);
      long classModifiedTime = coverage.getClassByteSource().getClassInfo(className).getLastModifiedTime();
      classInfoMap.put(className, ClassInfoVisitor.getClassInfo(className, classBytes, classModifiedTime));
    }
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfoMap);
  }
```
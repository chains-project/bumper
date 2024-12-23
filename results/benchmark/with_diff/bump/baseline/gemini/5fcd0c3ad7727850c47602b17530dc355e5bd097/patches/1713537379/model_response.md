```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    final Set<ClassName> classNames = Collections.singleton(data.getMutatedClass());
    final ClassInfoBuilder classInfoBuilder = coverage.getClassInfoBuilder();
    final List<ClassInfo> classInfos = new ArrayList<>();
    for (ClassName className : classNames) {
      final byte[] bytecode = coverage.getBytecode(className);
      final long checksum = coverage.getChecksum(className);
      classInfos.add(classInfoBuilder.getClassInfo(className, bytecode, checksum));
    }
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfos);
  }
```
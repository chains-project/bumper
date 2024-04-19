```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    final Set<ClassName> classSet = Collections.singleton(data.getMutatedClass());
    final List<ClassInfo> classInfoList = new ArrayList<>();
    for (ClassName className : classSet) {
      final byte[] bytecode = coverage.getBytecode(className);
      final long checksum = coverage.getChecksum(className);
      if (bytecode != null) {
        classInfoList.add(ClassInfoVisitor.getClassInfo(className, bytecode, checksum));
      }
    }
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfoList);
  }
```
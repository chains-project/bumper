```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    final ClassName className = new ClassName(data.getFileName(), data.getMutatedClass());
    final byte[] bytecode = coverage.getClassBytecode(className);
    final long checksum = coverage.getClassChecksum(className);
    final ClassInfo classInfo = coverage.getClassInfoVisitor().getClassInfo(className, bytecode, checksum);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfo);
  }
```
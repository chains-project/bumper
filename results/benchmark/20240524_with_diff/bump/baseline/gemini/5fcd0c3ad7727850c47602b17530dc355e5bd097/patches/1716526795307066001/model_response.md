```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    final ClassName className = ClassName.fromString(data.getMutatedClass());
    byte[] bytecode = coverage.getBytecodeForClass(className);
    long checksum = coverage.getChecksumForClass(className);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), ClassInfoVisitor.getClassInfo(className, bytecode, checksum));
  }
```
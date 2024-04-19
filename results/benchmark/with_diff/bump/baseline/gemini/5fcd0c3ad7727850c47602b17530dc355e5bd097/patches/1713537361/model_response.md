```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    final ClassName className = new ClassName(data.getMutatedClass());
    final byte[] bytecode = data.getBytecode();
    final long checksum = data.getHash();
    final ClassInfo classInfo = ClassInfoVisitor.getClassInfo(className, bytecode, checksum);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfo);
  }
```
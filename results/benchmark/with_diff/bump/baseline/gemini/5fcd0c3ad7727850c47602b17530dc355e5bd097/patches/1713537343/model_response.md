```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    final String className = data.getMutatedClass();
    final byte[] classBytes = coverage.getBytecodeForClass(className);
    final long classId = coverage.getClassId(className);
    final ClassInfoBuilder classInfoBuilder =
        ClassInfoVisitor.getClassInfo(ClassName.fromString(className), classBytes, classId);
    final ClassInfo classInfo = classInfoBuilder.build();
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfo);
  }
```
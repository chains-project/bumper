```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassName mutatedClass = data.getMutatedClass();
    byte[] classBytes = coverage.getClassBytes(mutatedClass);
    long classId = coverage.getClassId(mutatedClass);
    ClassInfo classInfo = ClassInfoVisitor.getClassInfo(mutatedClass, classBytes, classId);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfo);
  }
```
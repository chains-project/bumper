```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassInfoVisitor classInfoVisitor = new ClassInfoVisitor();
    ClassName mutatedClass = data.getMutatedClass();
    byte[] classInfoBytes = {}; // Initialize as needed
    long classInfoLong = 0L; // Initialize as needed
    ClassInfoBuilder classInfoBuilder = ClassInfoVisitor.getClassInfo(mutatedClass, classInfoBytes, classInfoLong);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfoBuilder.build());
  }
```
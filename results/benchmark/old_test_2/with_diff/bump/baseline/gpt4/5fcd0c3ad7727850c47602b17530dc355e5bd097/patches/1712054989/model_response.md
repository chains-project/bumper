```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassName mutatedClass = data.getMutatedClass();
    byte[] classBytes = mutatedClass.getBytes();
    long classHash = mutatedClass.hashCode();
    ClassInfoBuilder classInfo = ClassInfoVisitor.getClassInfo(mutatedClass, classBytes, classHash);

    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfo);
  }
```
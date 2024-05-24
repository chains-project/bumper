```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassName className = data.getMutatedClass();
    byte[] classBytes = ...; // assume this is set correctly
    long timestamp = ...; // assume this is set correctly
    ClassInfo classInfo = ClassInfoVisitor.getClassInfo(className, classBytes, timestamp);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfo);
}
```
```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassName className = data.getMutatedClass();
    byte[] classBytes = ...; // assuming you have a way to get the class bytes
    long timestamp = ...; // assuming you have a way to get the timestamp
    ClassInfo classInfo = ClassInfoVisitor.getClassInfo(className, classBytes, timestamp);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfo);
}
```
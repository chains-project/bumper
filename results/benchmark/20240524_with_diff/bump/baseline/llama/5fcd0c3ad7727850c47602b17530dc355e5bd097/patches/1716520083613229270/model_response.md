```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassName className = data.getMutatedClass();
    byte[] classBytes =coverage.getClassBytes(className);
    long timestamp = coverage.getTimestamp(className);
    ClassInfo classInfo = ClassInfoVisitor.getClassInfo(className, classBytes, timestamp);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfo);
}
```
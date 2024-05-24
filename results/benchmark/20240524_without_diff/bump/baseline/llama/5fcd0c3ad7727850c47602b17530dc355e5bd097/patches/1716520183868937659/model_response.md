```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassName className = data.getMutatedClass();
    byte[] classBytes = data.getClassBytes();
    long timestamp = data.getTimestamp();
    ClassInfo classInfo = ClassInfoVisitor.getClassInfo(className, classBytes, timestamp);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfo);
}
```
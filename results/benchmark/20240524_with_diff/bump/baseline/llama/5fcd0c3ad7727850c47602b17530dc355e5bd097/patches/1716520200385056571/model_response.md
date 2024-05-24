```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassName className = data.getMutatedClass();
    byte[] bytes = new byte[0]; // assuming empty byte array, adjust according to your needs
    long timestamp = 0; // assuming 0, adjust according to your needs
    ClassInfo classInfo = ClassInfoVisitor.getClassInfo(className, bytes, timestamp);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfo);
}
```
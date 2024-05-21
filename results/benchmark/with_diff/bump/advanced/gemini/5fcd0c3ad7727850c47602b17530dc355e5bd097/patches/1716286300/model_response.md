```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    final var clazz = data.getMutatedClass();
    final var bytes = coverage.getClassInfo(clazz);
    final var timestamp = coverage.getClassBytecodeTimestamp(clazz);
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), org.pitest.classinfo.ClassInfoVisitor.getClassInfo(clazz.getName(), bytes, timestamp));
}
```
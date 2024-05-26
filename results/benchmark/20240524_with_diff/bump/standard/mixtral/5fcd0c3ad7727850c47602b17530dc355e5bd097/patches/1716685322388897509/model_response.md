```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    final var className = data.getMutatedClass();
    final var classPath = coverage.getNestedElements().stream()
            .filter(e -> e.getClassName().equals(className))
            .map(org.pitest.coverage.NestedElement::getFile)
            .findFirst()
            .map(org.pitest.util.InMemorySource::getPath)
            .orElseThrow(() -> new IllegalStateException("Class not found in coverage data: " + className));
    final var bytes = org.pitest.io.FileIO.getBytes(classPath);
    final var classInfo = org.pitest.classinfo.ClassInfo.fromPath(className, bytes, coverage.getTimestamp());
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```
```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    final org.pitest.classinfo.ClassName className = data.getMutatedClass();
    final byte[] bytes = coverage.getClassBytes(className);
    final long lastModified = coverage.getLastModifiedTime(className);
    final org.pitest.classinfo.ClassInfoBuilder classInfoBuilder = org.pitest.classinfo.ClassInfoVisitor.getClassInfo(className, bytes, lastModified);
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfoBuilder.getClassInfo());
}
```
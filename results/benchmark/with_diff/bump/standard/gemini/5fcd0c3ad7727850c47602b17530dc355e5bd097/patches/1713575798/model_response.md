```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    final org.pitest.classinfo.ClassName className = org.pitest.classinfo.ClassName.fromString(data.getFileName());
    final byte[] bytecode = coverage.getBytecode(className);
    final long time = coverage.getLastModifiedTime(className);
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfoVisitor().getClassInfo(className, bytecode, time));
}
```
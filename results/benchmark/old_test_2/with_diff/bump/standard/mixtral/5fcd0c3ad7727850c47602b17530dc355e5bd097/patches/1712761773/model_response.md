Here's a possible patch for the given client code:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), getClassInfoFromCoverage(coverage, data.getMutatedClass()));
}

private org.pitest.classinfo.ClassInfo getClassInfoFromCoverage(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.classinfo.ClassName className) {
    byte[] classfileData = coverage.getRawClassFileData(className);
    long timestamp = coverage.getTimestamp(className);
    return org.pitest.classinfo.ClassInfoVisitor.getClassInfo(className, classfileData, timestamp);
}
```
The patch introduces a new helper method `getClassInfoFromCoverage` that uses the new `getClassInfo` method from `ClassInfoVisitor` to get the `ClassInfo` object from the `CoverageDatabase`. The `createSummaryData` method is updated to call this new helper method instead of the removed `getClassInfo` method from `CoverageDatabase`.
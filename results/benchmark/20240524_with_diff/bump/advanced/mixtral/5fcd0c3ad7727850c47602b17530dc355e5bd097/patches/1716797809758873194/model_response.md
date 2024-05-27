Here's the proposed patch for the given client code:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), getClassInfoFromCoverage(coverage, data.getMutatedClass()));
}

private org.pitest.classinfo.ClassInfo getClassInfoFromCoverage(org.pitest.coverage.CoverageDatabase coverage, org.pitest.classinfo.ClassName className) {
    return org.pitest.classinfo.ClassInfoBuilder.fromClassname(className).withCoverage(coverage.getClassData(className).getCodeCoverage()).build();
}
```

The original `getClassInfo` method was removed from `CoverageDatabase`. I created a new helper method `getClassInfoFromCoverage` that uses the new `ClassInfoBuilder` to build `ClassInfo` using the available code coverage information.
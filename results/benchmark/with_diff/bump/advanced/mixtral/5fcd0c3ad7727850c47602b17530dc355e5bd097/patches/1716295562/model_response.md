Here is the proposed patch for the `createSummaryData` method:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), getClassInfoFromCoverage(coverage, data.getMutatedClass()));
}

private org.pitest.classinfo.ClassInfo getClassInfoFromCoverage(org.pitest.coverage.CoverageDatabase coverage, org.pitest.classinfo.ClassName className) {
    return org.pitest.classinfo.ClassInfoVisitor.getClassInfo(className, coverage.getRawCoverageData(className), coverage.getTimeStamp());
}
```

Explanation:

The `getClassInfo` method in `CoverageDatabase` has been removed in the new library version, so we need to find an alternative way to get the `ClassInfo` for the given class name.

Fortunately, the new library version has added a new static method `getClassInfo` in `ClassInfoVisitor` that can be used to create a `ClassInfo` object from a class name, raw coverage data, and timestamp.

Therefore, we can create a new helper method `getClassInfoFromCoverage` that takes a `CoverageDatabase` and a `ClassName` as input, and returns the corresponding `ClassInfo` object using the new `getClassInfo` method in `ClassInfoVisitor`.

We can then call this helper method from the `createSummaryData` method to get the `ClassInfo` object for the mutated class.
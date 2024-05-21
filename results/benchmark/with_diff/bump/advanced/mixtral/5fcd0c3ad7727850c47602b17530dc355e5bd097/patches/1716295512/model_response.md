Here is a possible patch for the code:
```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), getClassInfoFromCoverage(coverage, data.getMutatedClass()));
}

private org.pitest.classinfo.ClassInfo getClassInfoFromCoverage(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.classinfo.ClassName className) {
    return org.pitest.classinfo.ClassInfoVisitor.getClassInfo(className, coverage.getRawCoverageData(className), coverage.getTimestamp());
}
```
Explanation:
The original code calls `getClassInfo` method on `coverage` object, which is of type `org.pitest.coverage.CoverageDatabase`. However, this method is no longer available in the new library version.
To fix this, we need to find an alternative way to get the `ClassInfo` object for the given class name.
Fortunately, the new library version has added a new static method `getClassInfo` in `org.pitest.classinfo.ClassInfoVisitor` that takes a `ClassName`, a byte array, and a long value as arguments.
We can use this method to get the `ClassInfo` object for the given class name.
To do this, we need to first get the raw coverage data for the given class name from the `coverage` object, and then pass it along with the class name and the timestamp to the `getClassInfo` method.
This is what the `getClassInfoFromCoverage` method does.
We can then call this method from the `createSummaryData` method to get the `ClassInfo` object and pass it to the `MutationTestSummaryData` constructor.
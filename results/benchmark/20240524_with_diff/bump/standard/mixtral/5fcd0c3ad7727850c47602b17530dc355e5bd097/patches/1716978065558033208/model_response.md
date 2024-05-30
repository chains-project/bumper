Here's the proposed patch to fix the error:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    org.pitest.classinfo.ClassInfoBuilder builder = org.pitest.classinfo.ClassInfoVisitor.getClassInfo(data.getMutatedClass(), new byte[0], 0);
    org.pitest.classinfo.ClassInfo classInfo = builder.build();
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassCoverage(classInfo).getClassInfo());
}
```

In the above patch, we are using the new `getClassInfo` method added in `ClassInfoVisitor` to build a `ClassInfo` object from the mutated class name. Then, we use the `getClassCoverage` method from `CoverageDatabase` to get the `ClassCoverage` object for the `ClassInfo`. Finally, we extract the `ClassInfo` from the `ClassCoverage` object.

Note that the above patch assumes that the `ClassInfo` object obtained from `getClassInfo` method has the same information as the one obtained from the deprecated `getClassInfo` method in `CoverageDatabase`. If this is not the case, then further modifications may be necessary.
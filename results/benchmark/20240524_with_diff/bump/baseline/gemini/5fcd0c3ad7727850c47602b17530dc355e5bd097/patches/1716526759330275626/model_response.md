```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    // Create a ClassInfoBuilder instance using the new method
    final ClassInfoBuilder classInfoBuilder = coverage.getClassInfo(data.getMutatedClass());

    // Build the ClassInfo object
    final ClassInfo classInfo = classInfoBuilder.build();

    // Return the MutationTestSummaryData object with the updated classInfo
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
  }
```
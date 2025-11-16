import pandas as pd
import asyncio
import random
import time

# Step 1: Define a Task class
class Task:
    def __init__(self, task_id, name, duration, priority):
        self.task_id = task_id
        self.name = name
        self.duration = duration
        self.priority = priority
    
    async def execute(self):
        print(f"Executing task {self.task_id}: {self.name}")
        # Simulate task execution time
        await asyncio.sleep(self.duration)
        print(f"Completed task {self.task_id}: {self.name}")

# Step 2: Read the dataset using pandas
data = {
    'task_id': [1, 2, 3, 4, 5],
    'name': ['Task A', 'Task B', 'Task C', 'Task D', 'Task E'],
    'duration': [2, 1, 3, 2, 1],
    'priority': [1, 2, 1, 3, 2]
}
df = pd.DataFrame(data)

# Step 3: Process tasks concurrently using asyncio
async def process_tasks(tasks):
    await asyncio.gather(*(task.execute() for task in tasks))

tasks = [Task(row['task_id'], row['name'], row['duration'], row['priority']) for _, row in df.iterrows()]

# Step 4: Analyze the processed data
def analyze_data(df):
    total_duration = df['duration'].sum()
    average_duration_per_priority = df.groupby('priority')['duration'].mean()
    return total_duration, average_duration_per_priority

# Running the asyncio event loop
async def main():
    await process_tasks(tasks)

# Run the main function to start processing
if __name__ == "__main__":
    asyncio.run(main())
    total_duration, avg_duration_per_priority = analyze_data(df)
    print(f"Total Duration: {total_duration}")
    print("Average Duration per Priority:")
    print(avg_duration_per_priority)

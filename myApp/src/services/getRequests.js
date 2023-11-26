
export const getAccountData = async () => {
  try {
    const response = await fetch('http://localhost:4000/person');
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
  }
};

import React from 'react';
import { Typography } from  '@mui/material';
import { Button } from '@mui/material';


const App = () => {
    return(
        <div>
            <Typography variant='h1'align='center'>
                Hello World!
            </Typography>
            <Typography variant='h2'align='center'>
                <Button
                    color = 'primary'
                    size = 'large'
                    type = 'submit'
                    variant = 'contained'
                    >
                        Sign up
                    </Button>
            </Typography>
        </div>
    )
}

export default App;
